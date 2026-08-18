namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Application.Queries;
using PetShop.Catalog.Infrastructure.Repositories;
using PetShop.Catalog.Infrastructure.Caching;
using PetShop.Shared.Domain;

public class GetProductsHandler : IRequestHandler<GetProductsQuery, Result<Paging<ProductResponse>>>
{
    private readonly IProductRepository _productRepository;
    private readonly IProductCacheService _cacheService;

    public GetProductsHandler(
        IProductRepository productRepository,
        IProductCacheService cacheService)
    {
        _productRepository = productRepository;
        _cacheService = cacheService;
    }

    public async Task<Result<Paging<ProductResponse>>> Handle(GetProductsQuery request, CancellationToken cancellationToken)
    {
        var cacheKey = $"products:search={request.Search}:cat={request.CategoryId}:min={request.MinPrice}:max={request.MaxPrice}:p={request.Page}";

        var cached = await _cacheService.GetProductsCacheAsync(cacheKey, cancellationToken);
        if (cached != null)
            return Result<Paging<ProductResponse>>.Success(cached);

        var products = await _productRepository.GetProductsAsync(
            request.Search, request.CategoryId, request.MinPrice, request.MaxPrice,
            request.Page, request.PageSize, cancellationToken);

        var totalCount = await _productRepository.CountAsync(request.Search, request.CategoryId, request.MinPrice, request.MaxPrice, cancellationToken);

        var paging = new Paging<ProductResponse>(
            products.Select(MapToResponse),
            request.Page,
            request.PageSize,
            totalCount
        );

        await _cacheService.SetProductsCacheAsync(cacheKey, paging, TimeSpan.FromMinutes(5), cancellationToken);

        return Result<Paging<ProductResponse>>.Success(paging);
    }

    private static ProductResponse MapToResponse(PetShop.Catalog.Domain.Entities.Product product)
    {
        return new ProductResponse(
            product.Id,
            product.Name,
            product.Description,
            product.Price,
            new CategoryResponse(product.CategoryId, "", null, null),
            product.ImageUrl,
            product.Status,
            product.InventoryCount
        );
    }
}

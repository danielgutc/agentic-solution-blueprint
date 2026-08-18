namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Application.Queries;
using PetShop.Catalog.Infrastructure.Repositories;
using PetShop.Catalog.Infrastructure.Caching;

public class GetProductByIdHandler : IRequestHandler<GetProductByIdQuery, Result<ProductResponse>>
{
    private readonly IProductRepository _productRepository;
    private readonly IProductCacheService _cacheService;

    public GetProductByIdHandler(
        IProductRepository productRepository,
        IProductCacheService cacheService)
    {
        _productRepository = productRepository;
        _cacheService = cacheService;
    }

    public async Task<Result<ProductResponse>> Handle(GetProductByIdQuery request, CancellationToken cancellationToken)
    {
        var cacheKey = $"product:{request.Id}";

        var cached = await _cacheService.GetProductCacheAsync(cacheKey, cancellationToken);
        if (cached != null)
            return Result<ProductResponse>.Success(cached);

        var product = await _productRepository.GetByIdAsync(request.Id, cancellationToken);
        if (product == null || product.IsDeleted)
            return Result<ProductResponse>.Failure("Product not found.");

        var response = new ProductResponse(
            product.Id,
            product.Name,
            product.Description,
            product.Price,
            new CategoryResponse(product.CategoryId, "", null, null),
            product.ImageUrl,
            product.Status,
            product.InventoryCount
        );

        await _cacheService.SetProductCacheAsync(cacheKey, response, TimeSpan.FromMinutes(15), cancellationToken);

        return Result<ProductResponse>.Success(response);
    }
}

namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.Commands;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Repositories;

public class UpdateProductHandler : IRequestHandler<UpdateProductCommand, Result<ProductResponse>>
{
    private readonly IProductRepository _productRepository;
    private readonly ICategoryRepository _categoryRepository;
    private readonly IProductCacheService _cacheService;

    public UpdateProductHandler(
        IProductRepository productRepository,
        ICategoryRepository categoryRepository,
        IProductCacheService cacheService)
    {
        _productRepository = productRepository;
        _categoryRepository = categoryRepository;
        _cacheService = cacheService;
    }

    public async Task<Result<ProductResponse>> Handle(UpdateProductCommand request, CancellationToken cancellationToken)
    {
        var product = await _productRepository.GetByIdAsync(request.Id, cancellationToken);
        if (product == null || product.IsDeleted)
            return Result<ProductResponse>.Failure("Product not found.");

        if (request.CategoryId.HasValue)
        {
            var category = await _categoryRepository.GetByIdAsync(request.CategoryId.Value, cancellationToken);
            if (category == null)
                return Result<ProductResponse>.Failure("Category not found.");
        }

        product.Update(request.Name, request.Description, request.Price, request.CategoryId, request.ImageUrl);
        await _productRepository.UpdateAsync(product, cancellationToken);

        await _cacheService.ClearProductsCacheAsync();

        return Result<ProductResponse>.Success(MapToResponse(product));
    }

    private static ProductResponse MapToResponse(Product product)
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

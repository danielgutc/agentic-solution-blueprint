namespace PetShop.Catalog.Application.Handlers;

using MediatR;
using PetShop.Catalog.Application.Commands;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Repositories;

public class CreateProductHandler : IRequestHandler<CreateProductCommand, Result<ProductResponse>>
{
    private readonly IProductRepository _productRepository;
    private readonly ICategoryRepository _categoryRepository;
    private readonly IInventoryRepository _inventoryRepository;
    private readonly IProductCacheService _cacheService;

    public CreateProductHandler(
        IProductRepository productRepository,
        ICategoryRepository categoryRepository,
        IInventoryRepository inventoryRepository,
        IProductCacheService cacheService)
    {
        _productRepository = productRepository;
        _categoryRepository = categoryRepository;
        _inventoryRepository = inventoryRepository;
        _cacheService = cacheService;
    }

    public async Task<Result<ProductResponse>> Handle(CreateProductCommand request, CancellationToken cancellationToken)
    {
        var category = await _categoryRepository.GetByIdAsync(request.CategoryId, cancellationToken);
        if (category == null)
            return Result<ProductResponse>.Failure("Category not found.");

        var product = new Product(
            Guid.NewGuid(),
            request.Name.Trim(),
            request.Description.Trim(),
            request.Price,
            request.CategoryId,
            request.ImageUrl,
            request.InventoryCount
        );

        await _productRepository.CreateAsync(product, cancellationToken);

        if (request.InventoryCount > 0)
        {
            await _inventoryRepository.CreateAsync(new Inventory(Guid.NewGuid(), product.Id, request.InventoryCount), cancellationToken);
        }

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

namespace PetShop.Catalog.Infrastructure.Repositories;

using PetShop.Catalog.Domain.Entities;

public interface IProductRepository
{
    Task<PetShop.Catalog.Domain.Entities.Product?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default);
    Task<IEnumerable<PetShop.Catalog.Domain.Entities.Product>> GetProductsAsync(
        string? search, Guid? categoryId, decimal? minPrice, decimal? maxPrice,
        int page, int pageSize, CancellationToken cancellationToken = default);
    Task<int> CountAsync(string? search, Guid? categoryId, decimal? minPrice, decimal? maxPrice, CancellationToken cancellationToken = default);
    Task CreateAsync(PetShop.Catalog.Domain.Entities.Product product, CancellationToken cancellationToken = default);
    Task UpdateAsync(PetShop.Catalog.Domain.Entities.Product product, CancellationToken cancellationToken = default);
}

public interface ICategoryRepository
{
    Task<PetShop.Catalog.Domain.Entities.Category?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default);
    Task<IEnumerable<PetShop.Catalog.Domain.Entities.Category>> GetAllAsync(CancellationToken cancellationToken = default);
    Task CreateAsync(PetShop.Catalog.Domain.Entities.Category category, CancellationToken cancellationToken = default);
    Task UpdateAsync(PetShop.Catalog.Domain.Entities.Category category, CancellationToken cancellationToken = default);
}

public interface IInventoryRepository
{
    Task<PetShop.Catalog.Domain.Entities.Inventory?> GetByProductIdAsync(Guid productId, CancellationToken cancellationToken = default);
    Task CreateAsync(PetShop.Catalog.Domain.Entities.Inventory inventory, CancellationToken cancellationToken = default);
    Task UpdateAsync(PetShop.Catalog.Domain.Entities.Inventory inventory, CancellationToken cancellationToken = default);
}

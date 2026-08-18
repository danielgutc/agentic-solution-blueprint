namespace PetShop.Catalog.Infrastructure.Repositories;

using Microsoft.EntityFrameworkCore;
using PetShop.Catalog.Application.DTOs;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Data;
using PetShop.Shared.Domain;

public class ProductRepository : IProductRepository
{
    private readonly CatalogDbContext _context;

    public ProductRepository(CatalogDbContext context)
    {
        _context = context;
    }

    public async Task<PetShop.Catalog.Domain.Entities.Product?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
    {
        return await _context.Products
            .FirstOrDefaultAsync(p => p.Id == id && !p.IsDeleted, cancellationToken);
    }

    public async Task<IEnumerable<PetShop.Catalog.Domain.Entities.Product>> GetProductsAsync(
        string? search, Guid? categoryId, decimal? minPrice, decimal? maxPrice,
        int page, int pageSize, CancellationToken cancellationToken = default)
    {
        var query = _context.Products
            .Where(p => !p.IsDeleted && p.Status != ProductStatus.OutOfStock)
            .AsQueryable();

        if (!string.IsNullOrWhiteSpace(search))
            query = query.Where(p => EF.Functions.ILike(p.Name, $"%{search}%"));

        if (categoryId.HasValue)
            query = query.Where(p => p.CategoryId == categoryId.Value);

        if (minPrice.HasValue)
            query = query.Where(p => p.Price >= minPrice.Value);

        if (maxPrice.HasValue)
            query = query.Where(p => p.Price <= maxPrice.Value);

        return await query
            .OrderBy(p => p.Name)
            .Skip((page - 1) * pageSize)
            .Take(pageSize)
            .ToListAsync(cancellationToken);
    }

    public async Task<int> CountAsync(string? search, Guid? categoryId, decimal? minPrice, decimal? maxPrice, CancellationToken cancellationToken = default)
    {
        var query = _context.Products
            .Where(p => !p.IsDeleted && p.Status != ProductStatus.OutOfStock)
            .AsQueryable();

        if (!string.IsNullOrWhiteSpace(search))
            query = query.Where(p => EF.Functions.ILike(p.Name, $"%{search}%"));
        if (categoryId.HasValue)
            query = query.Where(p => p.CategoryId == categoryId.Value);
        if (minPrice.HasValue)
            query = query.Where(p => p.Price >= minPrice.Value);
        if (maxPrice.HasValue)
            query = query.Where(p => p.Price <= maxPrice.Value);

        return await query.CountAsync(cancellationToken);
    }

    public async Task CreateAsync(PetShop.Catalog.Domain.Entities.Product product, CancellationToken cancellationToken = default)
    {
        await _context.Products.AddAsync(product, cancellationToken);
    }

    public async Task UpdateAsync(PetShop.Catalog.Domain.Entities.Product product, CancellationToken cancellationToken = default)
    {
        _context.Products.Update(product);
    }
}

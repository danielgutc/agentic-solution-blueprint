namespace PetShop.Catalog.Infrastructure.Repositories;

using Microsoft.EntityFrameworkCore;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Data;

public class CategoryRepository : ICategoryRepository
{
    private readonly CatalogDbContext _context;

    public CategoryRepository(CatalogDbContext context)
    {
        _context = context;
    }

    public async Task<PetShop.Catalog.Domain.Entities.Category?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default)
    {
        return await _context.Categories
            .FirstOrDefaultAsync(c => c.Id == id && !c.IsDeleted, cancellationToken);
    }

    public async Task<IEnumerable<PetShop.Catalog.Domain.Entities.Category>> GetAllAsync(CancellationToken cancellationToken = default)
    {
        return await _context.Categories
            .Where(c => !c.IsDeleted)
            .OrderBy(c => c.Name)
            .ToListAsync(cancellationToken);
    }

    public async Task CreateAsync(PetShop.Catalog.Domain.Entities.Category category, CancellationToken cancellationToken = default)
    {
        await _context.Categories.AddAsync(category, cancellationToken);
    }

    public async Task UpdateAsync(PetShop.Catalog.Domain.Entities.Category category, CancellationToken cancellationToken = default)
    {
        _context.Categories.Update(category);
    }
}

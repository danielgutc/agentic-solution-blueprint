namespace PetShop.Catalog.Infrastructure.Repositories;

using Microsoft.EntityFrameworkCore;
using PetShop.Catalog.Domain.Entities;
using PetShop.Catalog.Infrastructure.Data;

public class InventoryRepository : IInventoryRepository
{
    private readonly CatalogDbContext _context;

    public InventoryRepository(CatalogDbContext context)
    {
        _context = context;
    }

    public async Task<PetShop.Catalog.Domain.Entities.Inventory?> GetByProductIdAsync(Guid productId, CancellationToken cancellationToken = default)
    {
        return await _context.Inventories
            .FirstOrDefaultAsync(i => i.ProductId == productId, cancellationToken);
    }

    public async Task CreateAsync(PetShop.Catalog.Domain.Entities.Inventory inventory, CancellationToken cancellationToken = default)
    {
        await _context.Inventories.AddAsync(inventory, cancellationToken);
    }

    public async Task UpdateAsync(PetShop.Catalog.Domain.Entities.Inventory inventory, CancellationToken cancellationToken = default)
    {
        _context.Inventories.Update(inventory);
    }
}

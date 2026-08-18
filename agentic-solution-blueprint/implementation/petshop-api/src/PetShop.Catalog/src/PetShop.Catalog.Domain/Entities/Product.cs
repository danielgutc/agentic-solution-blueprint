namespace PetShop.Catalog.Domain.Entities;

public class Product : PetShop.Shared.Domain.Entity<Guid>
{
    public string Name { get; private set; }
    public string Description { get; private set; }
    public decimal Price { get; private set; }
    public Guid CategoryId { get; private set; }
    public string? ImageUrl { get; private set; }
    public ProductStatus Status { get; private set; }
    public int InventoryCount { get; private set; }

    public Product()
    {
        Name = string.Empty;
        Description = string.Empty;
        Price = 0m;
        CategoryId = Guid.Empty;
        Status = ProductStatus.Active;
        InventoryCount = 0;
    }

    public Product(Guid id, string name, string description, decimal price, Guid categoryId, string? imageUrl, int inventoryCount)
    {
        Id = id;
        Name = name;
        Description = description;
        Price = price;
        CategoryId = categoryId;
        ImageUrl = imageUrl;
        Status = ProductStatus.Active;
        InventoryCount = inventoryCount;
    }

    public void Update(string? name, string? description, decimal? price, Guid? categoryId, string? imageUrl)
    {
        if (name is not null && name != Name)
            Name = name.Trim();
        if (description is not null && description != Description)
            Description = description.Trim();
        if (price is not null && price != Price)
            Price = price.Value;
        if (categoryId is not null && categoryId != CategoryId)
            CategoryId = categoryId.Value;
        if (imageUrl is not null && imageUrl != ImageUrl)
            ImageUrl = imageUrl;
        MarkUpdated();
    }

    public void SetStatus(ProductStatus status)
    {
        Status = status;
        MarkUpdated();
    }

    public void AdjustInventory(int quantity)
    {
        InventoryCount += quantity;
        if (InventoryCount <= 0)
            Status = ProductStatus.OutOfStock;
        else if (Status == ProductStatus.OutOfStock && InventoryCount > 0)
            Status = ProductStatus.Active;
        MarkUpdated();
    }

    public bool IsAvailable => Status == ProductStatus.Active && InventoryCount > 0;
}

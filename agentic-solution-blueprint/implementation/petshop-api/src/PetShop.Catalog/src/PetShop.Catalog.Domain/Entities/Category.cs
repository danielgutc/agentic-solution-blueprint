namespace PetShop.Catalog.Domain.Entities;

public class Category : PetShop.Shared.Domain.Entity<Guid>
{
    public string Name { get; private set; }
    public string? Description { get; private set; }
    public Guid? ParentCategoryId { get; private set; }

    public Category()
    {
        Name = string.Empty;
    }

    public Category(Guid id, string name, string? description = null, Guid? parentCategoryId = null)
    {
        Id = id;
        Name = name;
        Description = description;
        ParentCategoryId = parentCategoryId;
    }

    public void Update(string name, string? description, Guid? parentCategoryId)
    {
        Name = name.Trim();
        Description = description?.Trim();
        ParentCategoryId = parentCategoryId;
        MarkUpdated();
    }
}

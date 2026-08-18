namespace PetShop.Catalog.Application.DTOs;

public record CategoryResponse(
    Guid Id,
    string Name,
    string? Description,
    Guid? ParentCategoryId
);

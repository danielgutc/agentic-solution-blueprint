namespace PetShop.Catalog.Application.DTOs;

public record ProductResponse(
    Guid Id,
    string Name,
    string Description,
    decimal Price,
    CategoryResponse Category,
    string? ImageUrl,
    ProductStatus Status,
    int InventoryCount
);

public record ProductListResponse(
    IEnumerable<ProductResponse> Items,
    int TotalCount,
    int Page,
    int PageSize,
    bool HasNextPage
);

public record CreateProductRequest(
    string Name,
    string Description,
    decimal Price,
    Guid CategoryId,
    string? ImageUrl,
    int InventoryCount
);

public record UpdateProductRequest(
    string? Name,
    string? Description,
    decimal? Price,
    Guid? CategoryId,
    string? ImageUrl
);

public record SearchProductsRequest(
    string? Search,
    Guid? CategoryId,
    decimal? MinPrice,
    decimal? MaxPrice,
    int Page = 1,
    int PageSize = 20
);

using MediatR;
using PetShop.Catalog.Application.DTOs;

namespace PetShop.Catalog.Application.Commands;

public record CreateProductCommand(
    string Name,
    string Description,
    decimal Price,
    Guid CategoryId,
    string? ImageUrl,
    int InventoryCount
) : IRequest<Result<ProductResponse>>;

public record UpdateProductCommand(
    Guid Id,
    string? Name,
    string? Description,
    decimal? Price,
    Guid? CategoryId,
    string? ImageUrl
) : IRequest<Result<ProductResponse>>;

public record DeleteProductCommand(Guid Id) : IRequest<Result>;

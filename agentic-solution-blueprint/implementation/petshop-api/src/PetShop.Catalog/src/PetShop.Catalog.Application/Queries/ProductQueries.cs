using MediatR;
using PetShop.Catalog.Application.DTOs;

namespace PetShop.Catalog.Application.Queries;

public record GetProductsQuery(
    string? Search,
    Guid? CategoryId,
    decimal? MinPrice,
    decimal? MaxPrice,
    int Page = 1,
    int PageSize = 20
) : IRequest<Result<Paging<ProductResponse>>>;

public record GetProductByIdQuery(Guid Id) : IRequest<Result<ProductResponse>>;

public record GetCategoriesQuery : IRequest<Result<IEnumerable<CategoryResponse>>>;

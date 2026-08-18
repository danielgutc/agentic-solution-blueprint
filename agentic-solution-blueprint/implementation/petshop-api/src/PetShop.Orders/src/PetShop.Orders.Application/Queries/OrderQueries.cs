namespace PetShop.Orders.Application.Queries;

using MediatR;
using PetShop.Orders.Application.DTOs;

public record GetOrdersQuery(
    Guid UserId,
    string? StatusFilter,
    int Page = 1,
    int PageSize = 20
) : IRequest<Result<OrderListResponse>>;

public record GetOrderByIdQuery(
    Guid OrderId,
    Guid RequestingUserId
) : IRequest<Result<OrderResponse>>;

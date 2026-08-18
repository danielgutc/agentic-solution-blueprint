namespace PetShop.Orders.Application.Commands;

using MediatR;
using PetShop.Orders.Application.DTOs;

public record PlaceOrderCommand(
    Guid CustomerId,
    Guid CartId
) : IRequest<Result<OrderResponse>>;

public record UpdateOrderStatusCommand(
    Guid OrderId,
    OrderStatus Status
) : IRequest<Result<OrderResponse>>;

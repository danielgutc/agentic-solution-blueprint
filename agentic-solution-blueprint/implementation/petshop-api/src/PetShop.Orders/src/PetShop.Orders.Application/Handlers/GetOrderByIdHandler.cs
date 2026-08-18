namespace PetShop.Orders.Application.Handlers;

using MediatR;
using PetShop.Orders.Application.DTOs;
using PetShop.Orders.Application.Queries;
using PetShop.Orders.Infrastructure.Repositories;

public class GetOrderByIdHandler : IRequestHandler<GetOrderByIdQuery, Result<OrderResponse>>
{
    private readonly IOrderRepository _orderRepository;

    public GetOrderByIdHandler(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }

    public async Task<Result<OrderResponse>> Handle(GetOrderByIdQuery request, CancellationToken cancellationToken)
    {
        var order = await _orderRepository.GetByIdAsync(request.OrderId, cancellationToken);
        if (order == null)
            return Result<OrderResponse>.Failure("Order not found.");

        return Result<OrderResponse>.Success(MapToResponse(order));
    }

    private static OrderResponse MapToResponse(PetShop.Orders.Domain.Entities.Order order)
    {
        return new OrderResponse(
            order.Id, order.OrderNumber, order.CustomerId,
            order.Status, order.TotalAmount, order.Currency,
            order.Items.Select(i => new OrderItemResponse(
                i.ProductId, i.ProductName, i.Quantity, i.UnitPrice, i.TotalPrice)),
            order.CreatedAt);
    }
}

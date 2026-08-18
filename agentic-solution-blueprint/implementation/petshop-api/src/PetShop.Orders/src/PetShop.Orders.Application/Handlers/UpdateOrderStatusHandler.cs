namespace PetShop.Orders.Application.Handlers;

using MediatR;
using PetShop.Orders.Application.Commands;
using PetShop.Orders.Application.DTOs;
using PetShop.Orders.Domain.Entities;
using PetShop.Orders.Infrastructure.Repositories;

public class UpdateOrderStatusHandler : IRequestHandler<UpdateOrderStatusCommand, Result<OrderResponse>>
{
    private readonly IOrderRepository _orderRepository;

    public UpdateOrderStatusHandler(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }

    public async Task<Result<OrderResponse>> Handle(UpdateOrderStatusCommand request, CancellationToken cancellationToken)
    {
        var order = await _orderRepository.GetByIdAsync(request.OrderId, cancellationToken);
        if (order == null)
            return Result<OrderResponse>.Failure("Order not found.");

        order.UpdateStatus(request.Status);
        await _orderRepository.UpdateAsync(order, cancellationToken);

        return Result<OrderResponse>.Success(MapToResponse(order));
    }

    private static OrderResponse MapToResponse(Order order)
    {
        return new OrderResponse(
            order.Id, order.OrderNumber, order.CustomerId,
            order.Status, order.TotalAmount, order.Currency,
            order.Items.Select(i => new OrderItemResponse(
                i.ProductId, i.ProductName, i.Quantity, i.UnitPrice, i.TotalPrice)),
            order.CreatedAt);
    }
}

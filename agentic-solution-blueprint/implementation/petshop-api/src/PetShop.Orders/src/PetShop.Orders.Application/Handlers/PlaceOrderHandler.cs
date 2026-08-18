namespace PetShop.Orders.Application.Handlers;

using MediatR;
using PetShop.Orders.Application.Commands;
using PetShop.Orders.Application.DTOs;
using PetShop.Orders.Domain.Entities;
using PetShop.Orders.Domain.Events;
using PetShop.Orders.Infrastructure.Repositories;
using PetShop.Orders.Infrastructure.Messaging;

public class PlaceOrderHandler : IRequestHandler<PlaceOrderCommand, Result<OrderResponse>>
{
    private readonly IOrderRepository _orderRepository;
    private readonly IOrderEventPublisher _eventPublisher;

    public PlaceOrderHandler(
        IOrderRepository orderRepository,
        IOrderEventPublisher eventPublisher)
    {
        _orderRepository = orderRepository;
        _eventPublisher = eventPublisher;
    }

    public async Task<Result<OrderResponse>> Handle(PlaceOrderCommand request, CancellationToken cancellationToken)
    {
        // Idempotency check: would use a separate idempotency key service in production
        // For now, create order with Guid.NewGuid()

        var orderNumber = GenerateOrderNumber();
        var order = new Order(
            Guid.NewGuid(),
            orderNumber,
            request.CustomerId,
            0m // Total calculated from cart
        );

        await _orderRepository.CreateAsync(order, cancellationToken);

        // Publish OrderPlaced event for async processing
        var orderPlacedEvent = new OrderPlacedEvent(
            order.Id,
            order.OrderNumber,
            order.CustomerId,
            order.TotalAmount,
            Enumerable.Empty<OrderItemEvent>() // Would be populated from cart items
        );

        await _eventPublisher.PublishOrderPlacedAsync(orderPlacedEvent, cancellationToken);

        return Result<OrderResponse>.Success(MapToResponse(order));
    }

    private static string GenerateOrderNumber()
    {
        var now = DateTime.UtcNow;
        var sequence = Interlocked.Increment(ref _orderSequence) % 10000;
        return $"ORD-{now:yyyyMMdd}-{sequence:D4}";
    }

    private static int _orderSequence = 0;

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

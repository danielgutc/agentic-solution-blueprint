namespace PetShop.Orders.Infrastructure.Messaging;

using PetShop.Orders.Domain.Events;

public interface IOrderEventPublisher
{
    Task PublishOrderPlacedAsync(OrderPlacedEvent @event, CancellationToken cancellationToken = default);
    Task PublishOrderConfirmedAsync(OrderConfirmedEvent @event, CancellationToken cancellationToken = default);
    Task PublishOrderShippedAsync(OrderShippedEvent @event, CancellationToken cancellationToken = default);
}

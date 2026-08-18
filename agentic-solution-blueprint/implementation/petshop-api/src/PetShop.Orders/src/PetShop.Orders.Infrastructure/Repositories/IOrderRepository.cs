namespace PetShop.Orders.Infrastructure.Repositories;

using PetShop.Orders.Domain.Entities;

public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(Guid id, CancellationToken cancellationToken = default);
    Task<IEnumerable<Order>> GetByCustomerIdAsync(Guid customerId, int page, int pageSize, CancellationToken cancellationToken = default);
    Task<int> CountByCustomerIdAsync(Guid customerId, CancellationToken cancellationToken = default);
    Task CreateAsync(Order order, CancellationToken cancellationToken = default);
    Task UpdateAsync(Order order, CancellationToken cancellationToken = default);
}

public interface IOrderEventPublisher
{
    Task PublishOrderPlacedAsync(OrderPlacedEvent @event, CancellationToken cancellationToken = default);
    Task PublishOrderConfirmedAsync(OrderConfirmedEvent @event, CancellationToken cancellationToken = default);
    Task PublishOrderShippedAsync(OrderShippedEvent @event, CancellationToken cancellationToken = default);
}

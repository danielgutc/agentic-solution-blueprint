namespace PetShop.Catalog.Domain.Entities;

public class Inventory : PetShop.Shared.Domain.Entity<Guid>
{
    public Guid ProductId { get; private set; }
    public int Quantity { get; private set; }
    public int ReservedQuantity { get; private set; }

    public int AvailableQuantity => Quantity - ReservedQuantity;

    public Inventory()
    {
        Quantity = 0;
        ReservedQuantity = 0;
    }

    public Inventory(Guid id, Guid productId, int quantity)
    {
        Id = id;
        ProductId = productId;
        Quantity = quantity;
        ReservedQuantity = 0;
    }

    public void AdjustQuantity(int delta)
    {
        if (Quantity + delta < 0)
            throw new PetShop.Shared.Domain.DomainException("Cannot reduce inventory below zero.");
        Quantity += delta;
        MarkUpdated();
    }

    public void Reserve(int quantity)
    {
        if (AvailableQuantity < quantity)
            throw new PetShop.Shared.Domain.DomainException("Insufficient available inventory.");
        ReservedQuantity += quantity;
        MarkUpdated();
    }

    public void ReleaseReservation(int quantity)
    {
        if (ReservedQuantity < quantity)
            throw new PetShop.Shared.Domain.DomainException("Cannot release more than reserved.");
        ReservedQuantity -= quantity;
        MarkUpdated();
    }

    public void ConfirmReservation(int quantity)
    {
        if (ReservedQuantity < quantity)
            throw new PetShop.Shared.Domain.DomainException("Cannot confirm more than reserved.");
        ReservedQuantity -= quantity;
        Quantity -= quantity;
        MarkUpdated();
    }
}

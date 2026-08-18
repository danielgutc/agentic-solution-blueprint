namespace PetShop.Users.Domain.Entities;

public class User : PetShop.Shared.Domain.Entity<Guid>
{
    public string Email { get; private set; }
    public string PasswordHash { get; private set; }
    public string FirstName { get; private set; }
    public string LastName { get; private set; }
    public string? Phone { get; private set; }
    public string? Address { get; private set; }
    public UserRole Role { get; private set; }

    public User()
    {
        Email = string.Empty;
        PasswordHash = string.Empty;
        FirstName = string.Empty;
        LastName = string.Empty;
        Role = UserRole.Customer;
    }

    public User(Guid id, string email, string passwordHash, string firstName, string lastName, UserRole role = UserRole.Customer)
    {
        Id = id;
        Email = email;
        PasswordHash = passwordHash;
        FirstName = firstName;
        LastName = lastName;
        Role = role;
    }

    public void UpdateProfile(string? firstName, string? lastName, string? phone, string? address)
    {
        if (firstName is not null) FirstName = firstName.Trim();
        if (lastName is not null) LastName = lastName.Trim();
        if (phone is not null) Phone = phone.Trim();
        if (address is not null) Address = address.Trim();
        MarkUpdated();
    }

    public bool HasRole(UserRole role) => Role == role;
}

namespace PetShop.Auth.Domain.Entities;

public class UserCredentials
{
    public Guid UserId { get; set; }
    public string Email { get; set; }
    public string PasswordHash { get; set; }
    public string RefreshToken { get; set; }
    public DateTime RefreshTokenExpiry { get; set; }
    public bool IsRevoked { get; set; }

    public UserCredentials()
    {
        Email = string.Empty;
        PasswordHash = string.Empty;
        RefreshToken = string.Empty;
    }

    public UserCredentials(Guid userId, string email, string passwordHash)
    {
        UserId = userId;
        Email = email;
        PasswordHash = passwordHash;
        RefreshToken = string.Empty;
        RefreshTokenExpiry = DateTime.MinValue;
        IsRevoked = false;
    }

    public bool IsTokenValid(string token)
    {
        return !IsRevoked && RefreshToken == token && RefreshTokenExpiry > DateTime.UtcNow;
    }

    public void SetRefreshToken(string token, TimeSpan expiry)
    {
        RefreshToken = token;
        RefreshTokenExpiry = DateTime.UtcNow + expiry;
        IsRevoked = false;
    }

    public void RevokeToken()
    {
        IsRevoked = true;
        RefreshToken = string.Empty;
        RefreshTokenExpiry = DateTime.MinValue;
    }
}

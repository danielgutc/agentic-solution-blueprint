namespace Example.Api;

/// <summary>Provides the current instant.</summary>
public interface IClock
{
    /// <summary>Reads the instant.</summary>
    /// <returns>The current instant.</returns>
    DateTimeOffset Now();
}

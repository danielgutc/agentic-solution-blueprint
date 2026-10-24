namespace Example.Api;

/// <summary>Formats clock values for display.</summary>
/// <remarks>The service keeps formatting separate from the time source.</remarks>
public sealed class ClockService : IClock
{
    /// <inheritdoc />
    public DateTimeOffset Now() => DateTimeOffset.UtcNow;

    /// <summary>Formats the value supplied by the clock.</summary>
    /// <param name="clock">The source of the instant.</param>
    /// <param name="format">The runtime format string.</param>
    /// <returns>The formatted instant.</returns>
    /// <exception cref="ArgumentException">The format string is invalid.</exception>
    /// <remarks>Use the caller-supplied clock.</remarks>
    public string Format(IClock clock, string format)
    {
        return clock.Now().ToString(format);
    }
}

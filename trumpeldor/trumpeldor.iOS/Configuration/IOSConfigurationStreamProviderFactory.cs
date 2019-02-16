using trumpeldor.Configuration;

namespace trumpeldor.iOS.Configuration
{
    public class IOSConfigurationStreamProviderFactory : IConfigurationStreamProviderFactory
    {
        public IConfigurationStreamProvider Create()
        {
            return new IOSConfigurationStreamProvider();
        }
    }
}
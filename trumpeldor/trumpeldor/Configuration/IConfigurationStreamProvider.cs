using System;
using System.IO;
using System.Threading.Tasks;

namespace trumpeldor.Configuration
{
    public interface IConfigurationStreamProvider : IDisposable
    {
        Task<Stream> GetStreamAsync();
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using NUnit.Framework;
using Xamarin.UITest;
using Xamarin.UITest.Queries;
using trumpeldor;

namespace UITest
{
    [TestFixture(Platform.Android)]
    public class AttractionTests //Tests for requirement 6
    {
        IApp app;
        Platform platform;

        public AttractionTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }
    }
}

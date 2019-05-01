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
    public class SystemStartTests //Tests for requirement 1
    {
        IApp app;
        Platform platform;

        public SystemStartTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }

        [Test]
        public void InfoOnStartTest()// requirement 1.1
        {
            //Act
            app.Tap("EnglishBtn");
            app.Tap("InfoBtn");

            //Assert
            Assert.IsTrue(true);
        }
    }
}

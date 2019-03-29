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
    public class LoginTests
    {
        IApp app;
        Platform platform;

        public LoginTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }

        [Test]
        public void AnonymusLoginTest()
        {
            //Arrange
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");

            //Act
            app.Tap("AnonymusLoginBtn");

            //Assert
            app.WaitFor(() => app.Query("EnterGroupName").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            var groupEntry = app.Query(x => x.Marked("EnterGroupName"));
            Assert.IsTrue(groupEntry != null && groupEntry[0].Text == "");
        }

    }
}

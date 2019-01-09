using System;
using System.IO;
using System.Linq;
using NUnit.Framework;
using Xamarin.UITest;
using Xamarin.UITest.Queries;

namespace UITest
{
    [TestFixture(Platform.Android)]
    //[TestFixture(Platform.iOS)]
    public class Tests
    {
        IApp app;
        Platform platform;

        public Tests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }

        [Test]
        public void AppLaunches()
        {
            app.Screenshot("First screen.");
        }

        [Test]
        public void TextHintTest()
        {
            //Arrange

            //Act
            app.Tap("ToHint");

            //Assert
            var appResult = app.Query("HintDisplay").First(result => result.Text == "this is a text hint");
            Assert.IsTrue(appResult != null, "label is not displaying the right result");
        }
    }
}


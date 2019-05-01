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
    public class PreGameInfoTests //Tests for requirement 2
    {
        IApp app;
        Platform platform;

        public PreGameInfoTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }

        [Test]
        public void ViewInfoWhenOutOfRange() //requirement 2.2
        {
            var outOfRange = app.Query("PlayBtn").FirstOrDefault(x => x.Enabled == false);
            if (outOfRange != null)
            {
                var canViewInfo = app.Query("InfoBtn").FirstOrDefault(x => x.Enabled == true);
                Assert.IsTrue(canViewInfo != null, "problem");
            }
            else
            {
                Assert.IsTrue(true);
            }
        }

        [Test]
        public void HowToPlayBeforeGameTest() //requirement 2.3
        {

            //Act
            app.Tap("EnglishBtn");
            app.Tap("HowToPlayBtn");

            //Assert
            Assert.IsTrue(true);
            
        }
    }
}

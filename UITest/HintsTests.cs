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
    public class HintsTests //Tests for requirement 6.9
    {
        IApp app;
        Platform platform;

        public HintsTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
        }

        public void ArrangeStart()
        {
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");
            app.Tap("AnonymusLoginBtn");
            app.WaitFor(() => app.Query("EnterGroupName").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.EnterText("EnterGroupName", "abc");
            app.Tap("Btn1Clicked");
            app.EnterText("EnterAge", "8");
            app.Tap("BtnStartTripClicked");
            app.WaitFor(() => app.Query("AddHintBtn").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
        }

        [Test]
        public void LessScoreAfterThreeHints() //requirement 6.9.6
        {
            //Arrange
            ArrangeStart();
            
            var currScore = app.Query("scoreLbl");
            Assert.IsTrue(currScore != null);
            string scoreBefore = currScore[0].Text;
            Assert.IsTrue(scoreBefore != null);
            double numericScoreBefore = Double.Parse(scoreBefore.Substring(7, scoreBefore.Length - 7));
            
            //Act
            app.Tap("AddHintBtn");
            app.Back();
            app.Tap("AddHintBtn");
            app.Back();
            app.Tap("AddHintBtn");
            app.Back();

            currScore = app.Query("scoreLbl");
            Assert.IsTrue(currScore != null);
            string scoreAfter = currScore[0].Text;
            Assert.IsTrue(scoreAfter != null);
            double numericScoreAfter = Double.Parse(scoreAfter.Substring(7, scoreAfter.Length - 7));


            //Assert
            Assert.IsTrue(numericScoreAfter < numericScoreBefore);
        } 

        [Test]
        public void LastHintIsMapTest()
        {
            //Arrange
            ArrangeStart();

            //Act
            app.Tap("AddHintBtn");
            app.Back();
            app.Tap("AddHintBtn");
            app.Back();
            app.Tap("AddHintBtn");
            app.Back();
            app.Tap("AddHintBtn");

            //Assert
            app.Query("viewMap");
            app.WaitFor(() => app.Query("viewMap").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
           // Assert.IsTrue(app.Query(("viewMap").FirstOrDefault()..Enabled);
            var mapShowing = app.Query("viewMap").FirstOrDefault();
            var mapShowing1 = app.Query("m").FirstOrDefault();
            Assert.IsTrue(mapShowing != null, "problem");
        }
    }
}

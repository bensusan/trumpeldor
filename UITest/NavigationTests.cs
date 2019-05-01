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
    public class NavigationTests //Tests for requirement 5
    {
        IApp app;
        Platform platform;

        public NavigationTests(Platform platform)
        {
            this.platform = platform;
        }

        [SetUp]
        public void BeforeEachTest()
        {
            app = AppInitializer.StartApp(platform);
            app.Device.SetLocation(0, 0);

        }

        public void TestsInit()
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
        public void PastLocationsDrawTest()// 5.1
        {
            //Arrange
            TestsInit();

            //Act
            System.Threading.Thread.Sleep(20000);
            bool flag = true;
            LocationController lc = LocationController.GetInstance();
            foreach(KeyValuePair<double, double> loc in lc.GetStoredPositionsAsPairs())
            {
                if (!(-0.1 <= loc.Key && loc.Key <= 0.1 && -0.1 <= loc.Value && loc.Value <= 0.1))
                    flag = false;
            }

            //Assert
            Assert.IsTrue(flag);
        }

        [Test]
        public void ShowScoreOnTrackFinish() //requirement 5.2
        {
            //Arrange
            TestsInit();
             app.Tap("DestinationBtn");
            //if continueTrack is available-click it
            // else click on mission -> american question -> correct ans
            // click continue track
            //if continue to longer track is available:
                //assert if the label contains score
                //else repeat
            
            app.Tap("MissionBtn");
            //american question
            //correct answer
            //continue track
            //assert


            //Act

            //Assert
        }

        [Test]
        public void CanViewHint() //requirement 5.6
        {
            TestsInit();
            app.Tap("AddHintBtn");

            var tst = app.Query("HintDisplay").FirstOrDefault(res => res.Text != "");
            Assert.IsTrue(tst != null, "problem");
        }

        [Test]
        public void CanViewHintsHistory() //requirement 5.9
        {
            //Arrange
            TestsInit();
            app.Tap("AddHintBtn");
            app.Back();
            //try to view the saved first hint
            app.Tap("Hint 1");
            var tst = app.Query("HintDisplay").FirstOrDefault(res => res.Text == "This is text hint for Attraction 1");
            Assert.IsTrue(tst != null, "problem");
            app.Back();
            //add another hint
            Assert.IsTrue(app.Query("AddHintBtn").FirstOrDefault().Enabled);
            app.Tap("AddHintBtn");
            app.Back();
            //try to view the saved first hint and the second saved hint
            app.Tap("Hint 1");
            var tst1 = app.Query("HintDisplay").FirstOrDefault(res => res.Text == "This is text hint for Attraction 1");
            Assert.IsTrue(tst1 != null, "problem");
            app.Back();

            app.Tap("Hint 2");
            var wv = app.Query(x => x.Marked("webView"));
            //Assert.IsTrue(wv.Length != 0);
            //var tst2 = app.Query("HintWebViewDisplay").FirstOrDefault(res => res.Text.Contains("http://132.72.23.64:12345/media/"));
            //Assert.IsTrue(tst2 != null, "problem");
            app.Back();
        }

        [Test]
        public void ContinueToLongerTrack() //requirement 5.13
        {
            TestsInit();
        }
    }
}

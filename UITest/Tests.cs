using System;
using System.IO;
using System.Linq;
using NUnit.Framework;
using Xamarin.UITest;
using Xamarin.UITest.Queries;
using trumpeldor;

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

       /* [Test]
        public void AppLaunches()
        {
            app.Screenshot("First screen.");
        }*/

       /* [Test]
        public void GroupCreation()
        {
            //Arrange
            app.EnterText("EnterGroupName", "abc");
            app.Tap("Btn1Clicked");
            app.EnterText("EnterAge", "8");

            //Act
            app.Tap("BtnStartTripClicked");

            //Assert
           // Assert.IsTrue(trumpeldor.Views.groupCreationPage.canProcceed == true);
            //var appResult = app.Query("HintDisplay").First(result => result.Text == "this is a text hint");
            //Assert.IsTrue(appResult != null, "label is not displaying the right result");
        }*/
        [Test]
        public void ViewInfoWhenOutOfRange() //requirement 2.2
        {
            var outOfRange= app.Query("PlayBtn").FirstOrDefault(x => x.Enabled == false);
            if(outOfRange != null)
            {
                var canViewInfo= app.Query("InfoBtn").FirstOrDefault(x => x.Enabled == true);
                Assert.IsTrue(canViewInfo != null, "problem");
            }
            else
            {
                Assert.IsTrue(true);
            }
        }

        [Test]
        public void ViewInfoBeforeGame() //requirement 2.3
        {

            //Act
            app.Tap("InfoBtn");

            //Assert
            var tst = app.Query("InfoTxt").FirstOrDefault(res => res.Text != "");
            Assert.IsTrue(tst != null, "problem");
        }

        [Test]
        public void UserInfoAtSignIn() //requirement 4.2
        {
            // all grop fields are empty
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");
            app.Tap("FacebookLoginBtn");
            app.WaitFor(() => app.Query("EnterGroupName").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.Tap("BtnStartTripClicked");

            var stayed = app.Query(x => x.Marked("EnterGroupName"));/*stayed at group creation page*/
            var moved = app.Query(x => x.Marked("AddHintBtn")); /* moved to next page (navigation page)*/
            Assert.IsTrue(stayed.Length != 0);//stayed
            Assert.IsFalse(moved.Length != 0);//not moved

            //some of the fields are empty
            app.EnterText("EnterAge", "8");
            app.EnterText("EnterGroupName", "");
            
            app.Tap("BtnStartTripClicked");

            var stayed1 = app.Query(x => x.Marked("EnterGroupName"));/*stayed at group creation page*/
            var moved1 = app.Query(x => x.Marked("AddHintBtn")); /* moved to next page (navigation page)*/
            Assert.IsTrue(stayed1.Length != 0);//stayed
            Assert.IsFalse(moved1.Length != 0);//not moved

            //some of the fields are empty
            app.Tap("Btn1Clicked");
            app.Tap("BtnStartTripClicked");

            var stayed2 = app.Query(x => x.Marked("EnterGroupName"));/*stayed at group creation page*/
            var moved2 = app.Query(x => x.Marked("AddHintBtn")); /* moved to next page (navigation page)*/
            Assert.IsTrue(stayed2.Length != 0);//stayed
            Assert.IsFalse(moved2.Length != 0);//not moved

            //all fields are full
            app.Tap("Btn1Clicked");
            app.EnterText("EnterGroupName", "abc");
            
            app.EnterText("EnterAge", "9");
            app.Tap("BtnStartTripClicked");

            var stayed3 = app.Query(x => x.Marked("EnterGroupName"));/*stayed at group creation page*/
            var moved3 = app.Query(x => x.Marked("AddHintBtn")); /* moved to next page (navigation page)*/
            Assert.IsTrue(moved3.Length != 0);//moved

        }

        [Test]
        public void CanViewHint() //requirement 5.6
        {
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");
            app.Tap("FacebookLoginBtn");
            app.WaitFor(() => app.Query("EnterGroupName").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.EnterText("EnterGroupName", "abc");
            app.Tap("Btn1Clicked");
            app.EnterText("EnterAge", "8");
            app.Tap("BtnStartTripClicked");
            app.WaitFor(() => app.Query("AddHintBtn").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.Tap("AddHintBtn");
            
            var tst = app.Query("HintDisplay").FirstOrDefault(res => res.Text != "");
            Assert.IsTrue(tst != null, "problem");
            
        }

        [Test]
        public void CanViewHintsHistory() //requirement 5.9
        {
            //Arrange
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");
            app.Tap("FacebookLoginBtn");
            app.WaitFor(() => app.Query("EnterGroupName").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.EnterText("EnterGroupName", "abc");
            app.Tap("Btn1Clicked");
            app.EnterText("EnterAge", "8");
            app.Tap("BtnStartTripClicked");
            //add hint for first time
            app.WaitFor(() => app.Query("AddHintBtn").FirstOrDefault().Enabled, timeout: TimeSpan.FromSeconds(1200));
            app.Tap("AddHintBtn");
            app.Back();
            //try to view the saved first hint
            app.Tap("Hint 1");
            var tst = app.Query("HintDisplay").FirstOrDefault(res => res.Text == "This is text hint for Attraction 1") ;
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
    }
}


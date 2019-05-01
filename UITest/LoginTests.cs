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
    public class LoginTests //Tests for requirement 4
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
        public void AnonymusLoginTest() //requirement 4.1 (3)
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

        [Test]
        public void UserInfoAtSignIn() //requirement 4.2
        {
            // all grop fields are empty
            app.Tap("EnglishBtn");
            app.Tap("PlayBtn");
            app.Tap("AnonymusLoginBtn");
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

            /*
            //some of the fields are empty
            app.Tap("Btn1Clicked");
            app.Tap("BtnStartTripClicked");

            var stayed2 = app.Query(x => x.Marked("EnterGroupName"));//stayed at group creation page
            var moved2 = app.Query(x => x.Marked("AddHintBtn")); // moved to next page (navigation page)
            Assert.IsTrue(stayed2.Length != 0);//stayed
            Assert.IsFalse(moved2.Length != 0);//not moved
            */

            //all fields are full
           // app.Tap("Btn1Clicked");
            app.EnterText("EnterGroupName", "abc");

            app.EnterText("EnterAge", "9");
            app.Tap("BtnStartTripClicked");

            var stayed3 = app.Query(x => x.Marked("EnterGroupName"));/*stayed at group creation page*/
            var moved3 = app.Query(x => x.Marked("AddHintBtn")); /* moved to next page (navigation page)*/
            Assert.IsTrue(moved3.Length != 0);//moved

        }

    }
}

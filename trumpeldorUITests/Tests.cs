using System;
using System.IO;
using System.Linq;
using NUnit.Framework;
using Xamarin.UITest;
using Xamarin.UITest.Queries;

namespace trumpeldorUITests
{
    [TestFixture(Platform.Android)]
    [TestFixture(Platform.iOS)]
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
        public void ShowTrackOnMapTest()
        {
            //TODO
        }

        [Test]
        public void ShareOnSocialNetworkTest()
        {
            //TODO
        }

        [Test]
        public void ScoreOnEndOfTrack()
        {
            //TODO
        }

        [Test]
        public void CurrentLocationOnMapTest()
        {
            //TODO
        }

        [Test]
        public void MoreInformationAboutTrackPointTest()
        {
            //TODO
        }

        [Test]
        public void AlertWhenUserOutOfBordersTest()
        {
            //TODO
        }

        [Test]
        public void UserOutOfBordersGetInformationTest()
        {
            //TODO
        }

        [Test]
        public void LocationAccsessTest()
        {
            //TODO
        }

        [Test]
        public void AddingIconToImageTest()
        {
            //TODO
        }

        [Test]
        public void SignUpTest()
        {
            //TODO
        }

        [Test]
        public void RequestConfirmationBeforeSavingImageTest()
        {
            //TODO
        }

        [Test]
        public void ShowingCluesOnNavigationTest()
        {
            //TODO
        }

        [Test]
        public void AddClueOnNavigationTest()
        {
            //TODO
        }

        [Test]
        public void FinalClueTrackLocationTest()
        {
            //TODO
        }

        [Test]
        public void FinalClueAlertTest()
        {
            //TODO
        }

        [Test]
        public void FailOnGameEffectOnScoreTest()
        {
            //TODO
        }

        [Test]
        public void MoreThanThreeCluesTest()
        {
            //TODO
        }

        [Test]
        public void LeadingTableOnEndOfTrackTest()
        {
            //TODO
        }

        [Test]
        public void AmericanQuestionWorngTwiceTest()
        {
            //TODO
        }

        [Test]
        public void ContinueToLongerTrackTest()
        {
            //TODO
        }

        [Test]
        public void LoginWithFacebookTest()
        {
            //TODO
        }

        [Test]
        public void LoginWithGoogleTest()
        {
            //TODO
        }

    }
}

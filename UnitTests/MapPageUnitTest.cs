using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using trumpeldor;
using Xamarin.Forms;
using Xamarin.Forms.Maps;

namespace UnitTests
{
    [TestClass]
    public class MapPageUnitTest : ContentPage
    {
        [TestMethod]
        public void deg2radTest()
        {
            Assert.IsTrue(trumpeldor.Views.MapPage.deg2rad(0) == 0);
        }

        [TestMethod]
        public void DistanceBetweenTest()
        {
            Assert.IsTrue(trumpeldor.Views.MapPage.DistanceBetween(51, 43, 15.34, 17.22) > 4584000 && trumpeldor.Views.MapPage.DistanceBetween(51, 43, 15.34, 17.22) < 4585000);
        }

        [TestMethod]
        public void initTests()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
        }

        [TestMethod]
        public void AnonymusLoginTest()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            gc.SignUp("shahar", "");
            Assert.IsTrue(gc.currentUser.name.Equals("shahar") && gc.currentUser.socialNetwork.Equals(""));
        }

        [TestMethod]
        public void addCurrLocationToMap()
        {
            Map map = new Map()
            {
                HeightRequest = 100,
                WidthRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            GameController gc;
            trumpeldor.App a = ((App)Application.Current);
            gc=a.getGameController();
            trumpeldor.Views.MapPage mp = new trumpeldor.Views.MapPage();
            //Assert.IsTrue(mp.currLat>=29 && mp.currLat<=30 && mp.currLong>=34.5 && mp.currLong<=35);
        }


        [TestMethod]
        public void CurrLocationTest()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            trumpeldor.SheredClasses.Point target = gc.GetUserLocation();
            Assert.IsTrue(target.x== 31.262880 && target.y== 34.801722);
        }

        [TestMethod]
        public void IsInBoundTest()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            Assert.IsTrue(gc.IsUserInValidSector());
        }

        [TestMethod]
        public void ClosestAttractionTest()
        {
            //Arrange
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            System.Collections.Generic.List<int> myAges = new System.Collections.Generic.List<int>();
            myAges.Add(9);
            myAges.Add(8);

            //Act
            gc.CreateTrip("testtrip group", myAges, 2);
            gc.currentTrip.
        }

        [TestMethod]
        public void TripTest()
        {
            //Arrange
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            System.Collections.Generic.List<int> myAges = new System.Collections.Generic.List<int>();
            myAges.Add(9);
            myAges.Add(8);

            //Act
            gc.CreateTrip("testtrip group", myAges, 2);
        }

    }
}

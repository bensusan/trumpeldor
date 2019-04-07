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
    }
}

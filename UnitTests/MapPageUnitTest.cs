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

    }
}

using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using trumpeldor;
using Xamarin.Forms;
using Xamarin.Forms.Maps;

namespace UnitTests
{
    [TestClass]
    class LocationTests : ContentPage
    {
        [TestMethod]
        public void CurrLocationTest()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            Assert.IsTrue(gc.GetUserLocation().Equals(new trumpeldor.SheredClasses.Point(31.262880, 34.801722)));
        }

        [TestMethod]
        public void IsInBoundTest()
        {
            ServerConnectionForTests sct = new ServerConnectionForTests();
            GameController gc = GameController.getInstance(sct);
            Assert.IsTrue(gc.IsUserInValidSector());
        }
    }
}

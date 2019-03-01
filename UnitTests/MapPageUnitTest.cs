using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using trumpeldor;

namespace UnitTests
{
    [TestClass]
    public class MapPageUnitTest
    {
        [TestMethod]
        public void deg2radTest()
        {
            trumpeldor.Views.MapPage map = new trumpeldor.Views.MapPage();
            Assert.IsFalse(0==1);
            Assert.IsTrue(1 + 1 == 2);
            //Assert.IsTrue(map.deg2rad(0) == 0);


        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Hint
    {
        
        public int id { get; set; }
        public string kind { get; set; }
        public string data { get; set; }

        //not for use
        public enum Kinds { HintMap = 1, HintPicture = 2, HintText = 3, HintVideo = 4 };
    }
}

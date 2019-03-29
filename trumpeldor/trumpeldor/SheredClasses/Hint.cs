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
        public enum Kinds { HintPicture, HintText, HintVideo };
        public static Dictionary<Kinds, string> kind2String = new Dictionary<Kinds, string>()
        {
            {Kinds.HintPicture, "HP"},
            {Kinds.HintText, "HT"},
            {Kinds.HintVideo, "HV"}
        };
    }
}

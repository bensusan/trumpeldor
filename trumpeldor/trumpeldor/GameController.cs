using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    public class GameController
    {
        public enum pathLength
        {
            shortPath = 1,
            mediumPath = 2,
            longPath = 3
        }

        public GameController()
        {
            
        }

        public void createGroup(string groupName, List<int> agesList)
        {
            //TODO
        }

        public int getScore()
        {
            return 0;
            //TODO
        }

        public void selectPath(pathLength selectedPathLength)
        {
            //TODO
        }
        public void selectNextTrackPoint()
        {
            //TODO
        }

        public Clue getClue()
        {
            //TODO
            return new TextClue();
        }
        public bool isCurrentTrackPointHasImage()
        {
            //TODO
            return false;
        }
        public String getCurrentTrackPointName()
        {
            //TODO
            return "track point name";
        }
        public Xamarin.Forms.ImageSource getCurrentTrackPointImage()
        {
            //TODO
            return null;
        }
        public bool isCurrentTrackPointHasAR()
        {
            //TODO
            return false;
        }
        public String getGeneralInformation()
        {
            //TODO
            return "some general information";
        }
        public String getCurrentTrackPointQuestion()
        {
            //TODO
            return "choose 1";
        }
        public bool isCurrentTrackPointHasQuestionImage()
        {
            //TODO
            return false;
        }
        public Xamarin.Forms.ImageSource getCurrentTrackPointQuestionImage()
        {
            //TODO
            return null;
        }
        public List<String> getCurrentTrackPointQuestionAnswers()
        {
            //TODO
            List<string> ans = new List<string>();ans.Add("1"); ans.Add("2"); ans.Add("3"); ans.Add("4");
            return ans;
        }
        public int getCurrentTrackPointCurrectAnswersToQuestion()
        {
            //TODO 
            return 0;
        }
        public bool isFinishTrack()
        {
            //TODO
            return true;
        }
        public bool canContinueToLongerTrack()
        {
            //TODO
            return false;
        }
        public void ContinueToLongerTrack()
        {
            //TODO
        }
    }
}

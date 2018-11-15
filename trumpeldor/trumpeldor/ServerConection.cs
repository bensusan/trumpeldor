using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    class ServerConection
    {
        public ServerConection()
        {

        }

        public List<TrackPoint> SelectPath(GameController.PathLength selectedPathLength)
        {
            //track point contain only id,Latitude,Longitude,name
            return new List<TrackPoint>()
            {
                new TrackPoint(31.262485, 34.803953),
                new TrackPoint(31.261930, 34.804132)
                
            };
            //TODO
        }
        public TrackPoint GetTrackPointById(string id)
        {
            //track point with all information
            return new TrackPoint(31.262485, 34.803953);
            //TODO
        }
        public List<Clue> GetTrackPointClues(string id)
        {
            return new List<Clue>();
            //TODO
        }
        public Game GetTrackPointGame(string id)
        {
            return new AQ();
            //TODO
        }
        public Game GetTrackPointAmericanQuestion(string id)
        {
            return new AQ();
            //TODO
        }

        public String GetGeneralInformation()
        {

            //TODO
            return "some general information";
        }
    }
}

<?php
echo '<html>
<meta name ="viewpoint" content = "width=device-width, initial-scale = 1.0"> 

<link href  = "css/tweetdisplay.css" rel = "stylesheet">
 <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
 
    <body>';
        
          outputTweets();
        echo 
        
    '</body>

</html>';

function outputTweets()
{
    $handle = fopen("Tweets.txt", "r");
    if ($handle)
    {
      echo '<h2>Featured Tweets</h2>
            <table style="width:100%" class="CSSTableGenerator">
                <tr>
                    <td><h3>Tweet Content</h3></td>
                    <td><h3>Title</h3></td>
                    <td><h3>Artist</h3></td>
                    <td><h3>Playlist</h3></td>
                </tr>';
      while (($tweet_content = fgets($handle)) !== false)
      {
          $song_name = fgets($handle);
          $artist = fgets($handle);
          $playlist_name = fgets($handle);
          $throw_away = fgets($handle);
          
          echo "<tr>
                    <td>$tweet_content</td>
                    <td>$song_name</td>
                    <td>$artist</td>
                    <td>$playlist_name</td>
                </tr>";
      }
    fclose($handle);
    echo '</table>';
    }
    else {
      echo '<p>Could not access the tweets.</p>';
    } 
}
?>

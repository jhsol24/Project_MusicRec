from django.db import models

# Create your models here.
class SongMeta(models.Model):
    song_id = models.IntegerField(primary_key=True)
    album_id = models.IntegerField(blank=True, null=True)
    album_name = models.CharField(max_length=200, blank=True, null=True)
    artist_id_basket = models.CharField(max_length=200, blank=True, null=True)
    artist_name_basket = models.CharField(max_length=200, blank=True, null=True)
    song_name = models.CharField(max_length=200, blank=True, null=True)
    song_gn_gnr_basket = models.CharField(max_length=200, blank=True, null=True)
    song_gn_dtl_gnr_basket = models.CharField(max_length=200, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    url_link = models.CharField(max_length=300, blank=True, null=True)
    album_image = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_meta'


class UserInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    age_group = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class Playlist(models.Model):
    playlist_id = models.CharField(primary_key=True, max_length=200)
    playlist_title = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    songs = models.CharField(max_length=300, blank=True, null=True)
    like_cnt = models.IntegerField(blank=True, null=True)
    updt_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlist'


class ReactionTable(models.Model):
    user = models.OneToOneField('UserInfo', models.DO_NOTHING, primary_key=True)
    song = models.ForeignKey('SongMeta', models.DO_NOTHING)
    reaction_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reaction_table'
        unique_together = (('user', 'song'),)
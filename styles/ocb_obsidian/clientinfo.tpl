<!-- OCB.GG client information. Uses TS3's documented template fields.
%%AVATAR_MAX_WIDTH%%96
%%AVATAR_MAX_HEIGHT%%96
Avatar and status icons are appended by the client; do not suppress them.
Optional fields must occupy a separate line for TS3's conditional replacement.
-->
<div class="InfoFrame">
<div class="InfoFrame_Title">
%%?CLIENT_COUNTRY_IMAGE_SCALED%%
<a class="TextMessage_UserLink" href="client://%%CLIENT_ID%%/%%CLIENT_UNIQUE_ID%%~%%CLIENT_NAME_PERCENT_ENCODED%%">%%CLIENT_NAME%%</a>
<span class="InfoFrame_CustomNick">[%%?CLIENT_CUSTOM_NICK_NAME%%]</span>
</div>
<hr />
<p><b>Identität</b></p>
<p><span class="Label">Eindeutige ID (UID)</span><br /><span style="font-family: monospace;">%%CLIENT_UNIQUE_ID%%</span></p>
<table class="InfoFrame_Table" cellspacing="0" cellpadding="3">
<tr><td class="Label">Client-ID (Sitzung)</td><td>%%CLIENT_ID%%</td></tr>
<tr><td class="Label">Datenbank-ID</td><td>%%?CLIENT_DATABASE_ID%%</td></tr>
</table>
<p><b>Verbindung &amp; Client</b></p>
<table class="InfoFrame_Table" cellspacing="0" cellpadding="3">
<tr><td class="Label">Version</td><td>%%?CLIENT_VERSION_LONG%%</td></tr>
<tr><td class="Label">Plattform</td><td>%%?CLIENT_PLATFORM%%</td></tr>
<tr><td class="Label">Online seit</td><td>%%?CLIENT_CONNECTED_SINCE%%</td></tr>
<tr><td class="Label">Erstmals verbunden</td><td>%%?CLIENT_CREATED%%</td></tr>
<tr><td class="Label">Zuletzt verbunden</td><td>%%?CLIENT_LASTCONNECTED%%</td></tr>
<tr><td class="Label">Verbindungen gesamt</td><td>%%?CLIENT_TOTALCONNECTIONS%%</td></tr>
<tr><td class="Label">Abwesend</td><td>%%?CLIENT_AWAY_MESSAGE%%</td></tr>
<tr><td class="Label">Lokale Lautstärke</td><td>%%?CLIENT_VOLUME_MODIFIER%% dB</td></tr>
</table>
<p><b>Beschreibung</b><br />%%?CLIENT_DESCRIPTION%%</p>
<p><b>Servergruppen</b></p>
<table class="InfoFrame_Table" cellspacing="0" cellpadding="3">
<tr><td>%%CLIENT_SERVER_GROUP_ICON%%</td><td>%%CLIENT_SERVER_GROUP_NAME%%</td></tr>
</table>
<p><b>Channelgruppe</b></p>
<table class="InfoFrame_Table" cellspacing="0" cellpadding="3">
<tr><td>%%CLIENT_CHANNEL_GROUP_ICON%%</td><td>%%CLIENT_CHANNEL_GROUP_NAME%%</td></tr>
</table>
%%??CLIENT_FLAG_BADGES%%<p><b>Abzeichen</b></p>
%%??CLIENT_FLAG_BADGES%%<table class="InfoFrame_Table" cellspacing="0" cellpadding="3">
%%??CLIENT_FLAG_BADGES%%<tr><td>%%CLIENT_BADGE_ICON_SMALL%%</td><td title="%%CLIENT_BADGE_DESCRIPTION%%">%%CLIENT_BADGE_NAME%%</td></tr>
%%??CLIENT_FLAG_BADGES%%</table>
<p class="Important"><b>Sprechwunsch</b><br />%%?CLIENT_TALK_REQUEST_TIME%%</p>
<p class="Important">%%?CLIENT_TALK_REQUEST_MSG%%</p>
<table class="InfoFrame_Table">%%?PLUGIN_INFO_DATA%%</table>
</div>

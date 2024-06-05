# Load the PluggableAuth extension
wfLoadExtension( 'PluggableAuth' );

# Load the OpenID Connect extension
wfLoadExtension( 'OpenIDConnect' );

# PluggableAuth configuration
$wgPluggableAuth_EnableAutoLogin = false; # Set to true if you want to enable auto-login
$wgPluggableAuth_EnableLocalLogin = true; # Set to false if you want to disable local login
$wgPluggableAuth_Class = 'OpenIDConnect';

# OpenID Connect configuration
$wgOpenIDConnect_Config = [
    [
        // Your OAuth2 provider configuration
        'clientID' => 'your-client-id',
        'clientsecret' => 'your-client-secret',
        'providerURI' => 'https://your-oauth2-provider',
        'redirectURI' => 'https://your-mediawiki-site/Special:PluggableAuthLogin',
        'scopes' => [ 'openid', 'profile', 'email' ],
        'authparam' => [ 'response_type' => 'code' ],
        'buttonLabelMessage' => 'Login with OAuth2', # Label for the login button
        'buttonCSSClass' => 'openidconnect', # CSS class for the login button
    ],
];

# Additional configuration (optional)
$wgOpenIDConnect_UseRealNameAsUsername = true; # Use the real name from the OAuth2 provider as the MediaWiki username
$wgOpenIDConnect_UseEmailNameAsUsername = false; # Use the email from the OAuth2 provider as the MediaWiki username
$wgOpenIDConnect_MigrateUsersByEmail = false; # Migrate users by email if they already exist in MediaWiki

# Logging (optional)
$wgDebugLogGroups['OpenIDConnect'] = "$IP/extensions/OpenIDConnect/OpenIDConnect.log";

# Ensure to adjust permissions if needed
$wgGroupPermissions['*']['autocreateaccount'] = true;
$wgGroupPermissions['*']['createaccount'] = false;
$wgGroupPermissions['*']['read'] = true; # or false depending on your wiki settings

# Uncomment the following lines if you encounter session issues
# $wgSessionCacheType = CACHE_DB;
# $wgMainCacheType = CACHE_NONE;
# $wgCacheDirectory = "$IP/cache";


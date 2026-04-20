diff --git a/chrome/install_static/chromium_install_modes.h b/chrome/install_static/chromium_install_modes.h
index ee62888f89705..7ec72d302bc4b 100644
--- a/chrome/install_static/chromium_install_modes.h
+++ b/chrome/install_static/chromium_install_modes.h
@@ -21,7 +21,7 @@ inline constexpr wchar_t kCompanyPathName[] = L"";

 // The brand-specific product name to be included as a component of the install
 // and user data directory paths.
-inline constexpr wchar_t kProductPathName[] = L"Chromium";
+inline constexpr wchar_t kProductPathName[] = L"Victoria";

 // The brand-specific safe browsing client name.
 inline constexpr char kSafeBrowsingName[] = "chromium";
@@ -44,48 +44,49 @@ inline constexpr auto kInstallModes = std::to_array<InstallConstants>({
             L"",  // Empty install_suffix for the primary install mode.
         .logo_suffix = L"",  // No logo suffix for the primary install mode.
         .app_guid =
-            L"",  // Empty app_guid since no integration with Google Update.
-        .base_app_name = L"Chromium",              // A distinct base_app_name.
-        .base_app_id = L"Chromium",                // A distinct base_app_id.
-        .browser_prog_id_prefix = L"ChromiumHTM",  // Browser ProgID prefix.
+            L"{DAC44AD6-9E68-4D70-94BA-5E7C5E60F511}",  // Victoria app GUID.
+        .base_app_name = L"Victoria",              // A distinct base_app_name.
+        .base_app_id = L"Victoria",                // A distinct base_app_id.
+        .browser_prog_id_prefix = L"VictHTML",  // Browser ProgID prefix.
         .browser_prog_id_description =
-            L"Chromium HTML Document",  // Browser ProgID description.
-        .direct_launch_url_scheme = "chromium",
-        .pdf_prog_id_prefix = L"ChromiumPDF",  // PDF ProgID prefix.
+            L"Victoria HTML Document",  // Browser ProgID description.
+        .direct_launch_url_scheme = "victoria",
+        .pdf_prog_id_prefix = L"VictPDF",  // PDF ProgID prefix.
         .pdf_prog_id_description =
-            L"Chromium PDF Document",  // PDF ProgID description.
+            L"Victoria PDF Document",  // PDF ProgID description.
         .active_setup_guid =
-            L"{7D2B3E1D-D096-4594-9D8F-A6667F12E0AC}",  // Active Setup
+            L"{5E3690F9-B55B-46A8-A58F-065C7041F184}",  // Active Setup
                                                         // GUID.
         .legacy_command_execute_clsid =
-            L"{A2DF06F9-A21A-44A8-8A99-8B9C84F29160}",  // CommandExecuteImpl
+            L"{D05C4DDB-B1C2-4174-AC04-2C4F88DAAE4D}",  // CommandExecuteImpl
                                                         // CLSID.
-        .toast_activator_clsid = {0x635EFA6F,
-                                  0x08D6,
-                                  0x4EC9,
-                                  {0xBD, 0x14, 0x8A, 0x0F, 0xDE, 0x97, 0x51,
-                                   0x59}},  // Toast Activator CLSID.
-        .elevator_clsid = {0xD133B120,
-                           0x6DB4,
-                           0x4D6B,
-                           {0x8B, 0xFE, 0x83, 0xBF, 0x8C, 0xA1, 0xB1,
-                            0xB0}},  // Elevator CLSID.
-        .elevator_iid = {0xbb19a0e5,
-                         0xc6,
-                         0x4966,
-                         {0x94, 0xb2, 0x5a, 0xfe, 0xc6, 0xfe, 0xd9,
-                          0x3a}},  // IElevator IID and TypeLib
-        // {BB19A0E5-00C6-4966-94B2-5AFEC6FED93A}.
-        .tracing_service_clsid = {0x83f69367,
-                                  0x442d,
-                                  0x447f,
-                                  {0x8b, 0xcc, 0x0e, 0x3f, 0x97, 0xbe, 0x9c,
-                                   0xf2}},  // SystemTraceSession CLSID.
-        .tracing_service_iid = {0xa3fd580a,
-                                0xffd4,
-                                0x4075,
-                                {0x91, 0x74, 0x75, 0xd0, 0xb1, 0x99, 0xd3,
-                                 0xcb}},  // ISystemTraceSessionChromium IID and
+        // Victoria: custom CLSIDs for Windows integration
+        .toast_activator_clsid = {0xBB42DE32,
+                                  0x5365,
+                                  0x49A6,
+                                  {0xB0, 0xDF, 0xA5, 0x45, 0x3D, 0x61, 0x78,
+                                   0x63}},  // Toast Activator CLSID.
+        .elevator_clsid = {0x40D0DF2B,
+                           0x6C1C,
+                           0x4018,
+                           {0x8B, 0x99, 0xB2, 0x91, 0xB2, 0x98, 0xCD,
+                            0xF2}},  // Elevator CLSID.
+        .elevator_iid = {0x5A8074B1,
+                         0x3645,
+                         0x497E,
+                         {0x92, 0xDC, 0x1B, 0x5F, 0x99, 0x44, 0xD2,
+                          0xAF}},  // IElevator IID and TypeLib
+        // {5A8074B1-3645-497E-92DC-1B5F9944D2AF}.
+        .tracing_service_clsid = {0xC511704D,
+                                  0x0BED,
+                                  0x4A46,
+                                  {0x95, 0x50, 0x7E, 0x07, 0x5E, 0xDD, 0xB8,
+                                   0xD0}},  // SystemTraceSession CLSID.
+        .tracing_service_iid = {0x631601BF,
+                                0x95A7,
+                                0x4ED1,
+                                {0x87, 0x93, 0x7C, 0x1E, 0xD5, 0x61, 0xC3,
+                                 0xE0}},  // ISystemTraceSessionChromium IID and
                                           // TypeLib
         .default_channel_name =
             L"",  // Empty default channel name since no update integration.

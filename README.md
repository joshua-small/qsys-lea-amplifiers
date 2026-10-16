# LEA Amplifiers - Custom Model Support for Q-SYS

An independently maintained custom fork of the LEA Connect Series amplifier plugin, with CS62/62D and CS122/122D support. Original source attribution to **Mike Matthews and Martin Velez** is retained; custom maintenance is by Joshua Small.

Plugin and package version: **1.4.2.9**.

## Install with Q-SYS Library

1. Sign in to [Q-SYS Library](https://library.qsys.com/my-library).
2. Open **My Packages → Add Personal Package**.
3. Enter **LEA Amplifiers - Custom Model Support** and this package URL:

   ```text
   https://joshua-small.github.io/qsys-lea-amplifiers/registration/joshuasmall.qsys.leaamplifiers/index.json
   ```

4. In Designer, sign in with the same QSC ID and open **Tools → Show Asset Installer**.
5. Refresh **Available Assets**, select the package and install it.

For manual installation, download `LeaAmplifierCustom.qplug` from [Releases](https://github.com/joshua-small/qsys-lea-amplifiers/releases) and place only that file in your Documents folder under `QSC/Q-Sys Designer/Plugins`. Keep backups and support files outside Plugins. Use one installation method to avoid duplicate copies. Refreshing/installing a package does not deploy changes to a Core; update and test the design before **Save to Core & Run**.

## Connect and operate

1. Add **LEA Amplifier > Custom Model Support** to a test design.
2. Choose the amplifier model and enter its IPv4 address.
3. The plugin connects using plain WebSocket on **port 1234**, path `/`.
4. Check subscriptions, controls and telemetry on the target amplifier. Confirm recovery after disconnecting and reconnecting.

Version 1.4.2.9 uses Q-SYS's native WebSocket API. Connection attempts time out after 10 seconds and retry after 5 seconds. Commands require a connected transport; offline commands are discarded and never replayed on reconnect. Sending a command does not establish device acknowledgement.

## Compatibility and attribution

Targets Q-SYS Designer/Core 10.5. Offline regression checks cover all 28 model choices. Native Designer/Core/device acceptance remains open. Inherited mic/line selections can reflect a local request rather than confirmed device feedback.

The retained original LEA sources include versions 1.3.2.0, 1.4.2.0 and 1.4.2.1; the earliest preserved custom copy is 1.4.2.3. The precise original fork point has not been established. This repository preserves the custom plugin identity and source attribution. It does not relicense upstream material.

## Support

Report bugs through [Issues](https://github.com/joshua-small/qsys-lea-amplifiers/issues), including plugin version, Q-SYS version, device/broker model and firmware, and reproduction steps. Remove credentials from logs and design files before sharing them.

This is an independent personal package, not a Q-SYS Verified Asset or a manufacturer-endorsed release. Manufacturer names and logos identify compatible products. Existing source attribution is retained.

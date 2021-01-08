---
title: 'PS: Write To Speech'
date: 2018-04-30T04:48:38+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-write-to-speech/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Use Powershell to get your computer to talk

### To Resolve:

1. So this is one of those things that you first start toying around with when you first start learning Powershell.

   ```powershell
   $Speaker = New-Object -ComObject Sapi.SpVoice
   $null = $Speaker.Speak($Text)
   ```

2. Use this code to remotely have another user hear what you type:

   ```powershell
   Enter-PSSession -ComputerName AHoleUser -Credential (Get-Credential)
   @'
   Add-Type -Language CsharpVersion3 -TypeDefinition @'
   using System.Runtime.InteropServices;
   [Guid("5CDF2C82-841E-4546-9722-0CF74078229A"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
   interface IAudioEndpointVolume {
   // f(), g(), ... are unused COM method slots. Define these if you care
   int f(); int g(); int h(); int i();
   int SetMasterVolumeLevelScalar(float fLevel, System.Guid pguidEventContext);
   int j();
   int GetMasterVolumeLevelScalar(out float pfLevel);
   int k(); int l(); int m(); int n();
   int SetMute([MarshalAs(UnmanagedType.Bool)] bool bMute, System.Guid pguidEventContext);
   int GetMute(out bool pbMute);
   }
   [Guid("D666063F-1587-4E43-81F1-B948E807363F"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
   interface IMMDevice {
   int Activate(ref System.Guid id, int clsCtx, int activationParams, out IAudioEndpointVolume aev);
   }
   [Guid("A95664D2-9614-4F35-A746-DE8DB63617E6"), InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
   interface IMMDeviceEnumerator {
   int f(); // Unused
   int GetDefaultAudioEndpoint(int dataFlow, int role, out IMMDevice endpoint);
   }
   [ComImport, Guid("BCDE0395-E52F-467C-8E3D-C4579291692E")] class MMDeviceEnumeratorComObject { }
   public class Audio {
   static IAudioEndpointVolume Vol() {
      var enumerator = new MMDeviceEnumeratorComObject() as IMMDeviceEnumerator;
      IMMDevice dev = null;
      Marshal.ThrowExceptionForHR(enumerator.GetDefaultAudioEndpoint(/*eRender*/ 0, /*eMultimedia*/ 1, out dev));
      IAudioEndpointVolume epv = null;
      var epvid = typeof(IAudioEndpointVolume).GUID;
      Marshal.ThrowExceptionForHR(dev.Activate(ref epvid, /*CLSCTX_ALL*/ 23, 0, out epv));
      return epv;
   }
   public static float Volume {
      get {float v = -1; Marshal.ThrowExceptionForHR(Vol().GetMasterVolumeLevelScalar(out v)); return v;}
      set {Marshal.ThrowExceptionForHR(Vol().SetMasterVolumeLevelScalar(value, System.Guid.Empty));}
   }
   public static bool Mute {
      get { bool mute; Marshal.ThrowExceptionForHR(Vol().GetMute(out mute)); return mute; }
      set { Marshal.ThrowExceptionForHR(Vol().SetMute(value, System.Guid.Empty)); }
   }
   }
   '@
   [Audio]::Mute = $false
   [Audio]::Volume = 1
   Add-Type -AssemblyName System.speech
   $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
   $speak.Speak('Hey everyone Im looking at porn over here, come check me out! This is why Im not productive')
   ```

3. I tested the following code in my lab and it worked! It takes a while to run, but it does work! I wouldn't ever do this though because it would unprofessional. Cool to learn though.

4. Source is maintained under [gwMisc](https://github.com/gerryw1389/powershell/blob/master/gwMisc/Public/Write-ToSpeech.ps1).
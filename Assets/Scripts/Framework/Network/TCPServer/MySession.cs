﻿using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using UnityEngine;

/// <summary>
/// 会话端
/// </summary>
public class MySession
{
    public Socket TcpSocket;//socket对象
    public List<byte> m_Buffer = new List<byte>();//数据缓存区

    public MySession()
    {

    }

    /// <summary>
    /// 发送数据
    /// </summary>
    /// <param name="buf"></param>
    public void Send(byte[] buf)
    {
        if (buf != null)
        {
            TcpSocket.Send(buf);
        }
    }
    /// <summary>
    /// 获取连接的ip
    /// </summary>
    /// <returns></returns>
    public string GetIp()
    {
        IPEndPoint clientipe = (IPEndPoint)TcpSocket.RemoteEndPoint;
        string _ip = clientipe.Address.ToString();
        return _ip;
    }
    /// <summary>
    /// 关闭连接
    /// </summary>
    public void Close()
    {
        TcpSocket.Shutdown(SocketShutdown.Both);
    }
    /// <summary>
    /// 提取正确数据包
    /// </summary>
    public byte[] GetBuffer(int startIndex, int size)
    {
        byte[] buf = new byte[size];
        m_Buffer.CopyTo(startIndex, buf, 0, size);
        m_Buffer.RemoveRange(0, startIndex + size);
        return buf;
    }

    /// <summary>
    /// 添加队列数据
    /// </summary>
    /// <param name="buffer"></param>
    public void AddQueue(byte[] buffer)
    {
        m_Buffer.AddRange(buffer);
    }
    /// <summary>
    /// 清除缓存
    /// </summary>
    public void ClearQueue()
    {
        m_Buffer.Clear();
    }
}
